function TreeNode(val, left=null, right=null) {
    this.val = val;
    this.left = left;
    this.right = right;
}

var sortedArrayToBST = function(nums) {
    if (!nums.length) return null;

    const buildBST = (left, right) => {
        if (left > right) return null;

        const mid = Math.floor((left + right) / 2);
        const node = new TreeNode(nums[mid]);

        node.left = buildBST(left, mid - 1);
        node.right = buildBST(mid + 1, right);

        return node;
    };

    return buildBST(0, nums.length - 1);
};