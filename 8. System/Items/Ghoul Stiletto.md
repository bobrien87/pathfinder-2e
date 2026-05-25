---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Agile]]", "[[Finesse]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *ghoul stiletto* is a *+1 dagger* wrapped in the still-undead skin of a ghoul. While you wield the dagger, you gain a +1 status bonus to all saves against curses and olfactory effects.

**Activate** `pf2:1` (concentrate, divine, manipulate, olfactory)

**Frequency** once per hour

**Effect** The ghoul stiletto afflicts the next living target struck by the dagger with a terrible wound that emits the foul stench of the grave. The creature emits a stench aura in a @Template[type:emanation|distance:10] for 1 minute. During that time, the affected creature, as well as any creature that starts or ends its turn in the aura, must succeed at a DC 17 [[Fortitude]] save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save is temporarily immune to all stench auras for 1 minute.

**Craft Requirements** The initial raw materials must include skin from a ghoul.

**Source:** `= this.source` (`= this.source-type`)
