---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]", "[[Vitality]]"]
price: "{'gp': 5}"
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

**Trigger** You succeed at, fail, or critically fail a recovery check while [[Dying]] by 1.

This pyrefowl feather, accentuated with beadwork, stores a spark of the bird's self-healing power. When you Activate the token, you reduce the triggering recovery check's DC by 1, potentially improving your check's degree of success. You also gain 5 temporary Hit Points that last for 1 minute. You can Activate this talisman even while [[Unconscious]].

**Source:** `= this.source` (`= this.source-type`)
