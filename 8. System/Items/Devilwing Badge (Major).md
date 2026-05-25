---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 1750}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small tearing of a devil's wing has been cleansed with holy water before being mounted onto a silver badge. The spell attack modifier of any spell cast by Activating this item is +19, and the spell DC is 29.

- **Armor** You gain resistance 10 to fire and unholy.
- **Weapon** After you cast a spell by Activating the *devilwing badge*, your Strikes with the weapon deal an additional 1d8 spirit damage until the end of your next turn.

> [!danger] Effect: Devilwing Badge (Armor)

> [!danger] Effect: Devilwing Badge (Weapon)

**Activate** Cast a Spell

**Effect** You cast [[Divine Lance]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 4th-rank [[Crisis of Faith]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Divine Wrath]].

**Source:** `= this.source` (`= this.source-type`)
