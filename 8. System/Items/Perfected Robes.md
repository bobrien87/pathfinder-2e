---
type: item
source-type: "Remaster"
level: "22"
traits: ["[[Artifact]]", "[[Divine]]", "[[Invested]]"]
price: "{'value': {}}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These unadorned white robes, fastened with simple brass pins in the shape of a human hand, can't be soiled or blemished. While wearing *perfected robes*, you don't need to eat, sleep, or drink, but you can if you choose to. The robes bless you with constant [[Truesight]] (+32 counteract bonus). A creature who dons these robes without earning them is [[Clumsy]] 3, [[Enfeebled]] 3, and [[Stupefied 3]] while wearing them, gaining the true seeing but otherwise unable to use the robes' magic.

**Activate** `pf2:f` (concentrate, fortune)

**Frequency** once per minute

**Effect** If your next action is to attempt a d20 roll with which you have legendary proficiency, roll twice and take the better result. This is a fortune effect.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You cast [[Avatar]], gaining the abilities for Irori.

**Destruction** If the wearer ever willingly turns from the path of self-perfection into corruption or overindulgence, their *perfected robes* crumble to nothing.

**Source:** `= this.source` (`= this.source-type`)
