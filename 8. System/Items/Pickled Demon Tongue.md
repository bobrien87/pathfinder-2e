---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Acid]]", "[[Divine]]", "[[Spellheart]]"]
price: "{'gp': 60}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small crystal vial contains the forked end of a demon's tongue, preserved in brine. The spell attack roll of any spell cast by Activating this item is +7, and the spell DC is 17.

- **Armor** You gain resistance 2 to acid and attacks by demons.
- **Weapon** After you cast an acid spell by Activating the *pickled demon tongue*, your Strikes with the weapon deal an additional 1d4 acid damage until end of your next turn.

> [!danger] Effect: Pickled Demon Tongue   Armor

> [!danger] Effect: Pickled Demon Tongue   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Caustic Blast]].

**Source:** `= this.source` (`= this.source-type`)
