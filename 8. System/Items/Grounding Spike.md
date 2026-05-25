---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Backswing]]", "[[Finesse]]", "[[Reach]]", "[[Sweep]]", "[[Versatile b]]"]
price: "{'gp': 950}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Metal caps the bottom of this *+1 striking thundering dancer's spear* and its point gives off the faint smell of ozone. If you hit a target that has been struck by a polarizing mace within the last round, you deal additional electricity damage to the target equal to the number of *grounding spike*'s damage dice. If you critically hit such a target, the creature is [[Off Guard]] until the start of your next turn.

**Special** The *grounding spike* pairs with the *[[Polarizing Mace]]*.

**Source:** `= this.source` (`= this.source-type`)
