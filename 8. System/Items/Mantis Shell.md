---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Adjusted]]"]
price: "{'gp': 10}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Construction of mantis shell armor originates with the Red Mantis assassins. Authentic mantis shell can be found in some dark markets, but wearing such armor can attract deadly attention from the armor's originators. Mantis shell comes with the weapon harness adjustment, though these special vambraces are meant to hold sawtooth sabers, and attaching anything else is an insult to the Red Mantis. A character who is a member of the Red Mantis assassins has access to this uncommon armor.

**Source:** `= this.source` (`= this.source-type`)
