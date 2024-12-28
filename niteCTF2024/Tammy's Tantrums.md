## Question 
Sometimes, venting is essential. I hope this platform becomes your go-to outlet in those moments of frustration.

## Solution
We are given a CRUD website wherein users can create short notes called "tantrums" which are displayed inside floating bubbles. Each tantrum must have a title and a description. Users can set the tantrum as private or public. Public tantrums are exhibited on the user's public profile at /<username> and can be accessed by anyone. Private tantrums can only be accessed by the tantrum's creator. The flag is located in the description of a private tantrum under the tammy user.

Upon analyzing the provided source code, we find a possible blind mongodb injection at the delete tantrum route src/app/api/v1/tantrums/[id]/route.ts wherein the tantrumId user input is being provided to a mongoose findOne() call without sanitization:

```typescript
const whereStr = `function() { return this._id === '${tantrumId}' }`;
const tantrum = await Tantrum.findOne({
    $where: whereStr,
});
if (!tantrum) {
    return errorResponse("Request failed", "Tantrum not found", 404);
} else if (tantrum.userId !== userId) {
    return errorResponse(
        "Request failed",
        "Tantrum belongs to another user",
        403
    );
}

const response = await Tantrum.findOneAndDelete({
    $where: whereStr,
});
if (!response) {
    return errorResponse("Request failed", "Failed to delete tantrum", 500);
}```
