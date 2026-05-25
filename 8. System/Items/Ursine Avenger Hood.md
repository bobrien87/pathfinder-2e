---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Artifact]]", "[[Invested]]", "[[Primal]]"]
price: "{'value': {}}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A gift passed from warrior to warrior, this cowl is made from a cave bear's skull and fur. Once invested, the wearer gains a +1 item bonus to Nature checks to [[Command an Animal]], which increases to +2 if the animal is a bear. The wearer of the hood feels a constant longing for the wilderness and wild places and takes a –1 item penalty to all Diplomacy checks to Gather Information or [[Make an Impression]] if they go more than 5 days inside a large town or city without spending at least 4 hours in the wilderness.

**Destruction** Soak the Ursine Avenger Hood in the blood of a linnorm that is at least 16th level and then burn it in a fire that uses only oak and chrysanthemum as fuel.

Ursine Avenger Hood

**Source:** `= this.source` (`= this.source-type`)
