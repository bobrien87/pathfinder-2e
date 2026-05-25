---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 230}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you pull up the hood of this nondescript gray cloak (an Interact action), you become drab and uninteresting, gaining a +1 item bonus to Stealth checks and to Deception checks to [[Impersonate]] a forgettable background character, such as a servant, but also taking a -1 item penalty to Diplomacy and Intimidation checks.

**Activate—Cloak Identity** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You pull the cloak's hood up and gain the benefits of [[Veil of Privacy]] for 1 hour or until you pull the hood back down, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
