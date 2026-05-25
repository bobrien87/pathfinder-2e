---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Scholarly journals are uncommon. Each scholarly journal is a folio on a very specific topic, such as vampires or the history of a single town or neighborhood of a city. If you spend 1 minute referencing an academic journal before attempting a skill check to Recall Knowledge about the subject, you gain a +1 item bonus to the check. A compendium of journals costs five times as much as a single journal and requires both hands to use; each compendium contains several journals and grants its bonus on a broader topic, such as all undead or a whole city. The GM determines what scholarly journals are available in any location.

**Source:** `= this.source` (`= this.source-type`)
