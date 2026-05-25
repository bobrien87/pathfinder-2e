---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornarmbands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Each of these shining, bluish-gray metal armbands is adorned with the plated visage of a gorgon's head. When targeted by a spell or effect with the incapacitation effect, you treat the result of your save as if it were one degree of success better, and the result of any check made to inflict such an effect on you as one degree of success worse (as if you were more than twice the rank of the spell or effect targeting you). When you invest the armbands, you either increase your Constitution modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You clap the bracers together and remove a single condition of your choice currently afflicting you. If the condition is permanent, it's instead suppressed for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
