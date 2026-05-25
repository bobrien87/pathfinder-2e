---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Artifact]]", "[[Divine]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This object, made of silver light, takes the form of a small musical instrument, prop, or other tool associated with a specific art form. The holder of the *immaculate instrument* never suffers from creative blocks of any kind and their work is always insightful and skilled. A character who uses the *immaculate instrument* to [[Perform]] or [[Craft]] can attempt the check at mythic proficiency once per month, and as long as they possess their *immaculate instrument*, they treat any critical failures with these skills as failures.

**Destruction** If the holder uses the *immaculate instrument* to intentionally produce a work that is not just mediocre or crass, but one that devalues the public opinion of the art form itself in a showing of at least 100 spectators, the instrument fades away in shame.

**Source:** `= this.source` (`= this.source-type`)
