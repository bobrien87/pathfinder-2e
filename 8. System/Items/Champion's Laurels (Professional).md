---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 160}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You are about to roll an Acrobatics or Athletics check, and you are trained or better in the skill

**Requirements** You can perceive at least 12 allies or friendly bystanders encouraging you.

This elegant crown of laurels can be worn on the head, atop a helmet, or even wrapped around the neck as a torc, signaling the wearer's athletic achievements in a past competition. When you Activate the laurels, you draw strength from your adoring crowd and gain a +2 status bonus to the triggering check. If you critically succeed at the check, you gain 10 temporary Hit Points that last for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
