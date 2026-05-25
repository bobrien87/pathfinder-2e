---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Censer]]", "[[Fire]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ceramic incense burner is shaped like a three-headed ibis in the form of Atreia, spreading his wings and preparing to take flight; it hangs on a thin, golden chain.

**Activate—Light Incense** `pf2:2` (aura, manipulate)

**Frequency** once per day

**Cost** incense worth at least 1 sp

**Effect** Sparkling golden mist escapes the ibis's open beaks, spreading in a @Template[emanation|distance:20]. This perfume mist is calming and restorative. A creature that ends its turn within the censer's smoke while sickened or under an affliction can attempt a new saving throw to overcome it.

A creature with multiple afflictions, or that is both sickened and has an affliction, chooses one to attempt to overcome each time it ends its turn in the aura. After attempting a new saving throw against an affliction, a creature is temporarily immune to *lambent perfume* for the purpose of overcoming that affliction for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
