function confirmDelEntry(obj) {
    let answer = confirm("Are you shure to delete this record from your log?");
    
    if (answer == false) {
        obj.href = "#";
    }
    return false;
}