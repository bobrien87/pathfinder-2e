---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Force]]", "[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 2600}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small figurine is carved from soapstone in the shape of a deity or guardian, facing both front and back to indicate unflagging vigilance. The spell attack modifier of any spell cast by activating this item is +20.

- **Armor** You gain resistance 5 against ranged weapon attacks.
- **Weapon** When you hit with a Strike using the affixed weapon, or when a spell effect you created by activating the statuette hits with a Strike, you can choose a creature adjacent to the creature that was hit. That creature gains a +1 status bonus to AC until the start of your next turn. No more than one creature can benefit from this each turn.

> [!danger] Effect: Warding Statuette   Armor

> [!danger] Effect: Warding Statuette   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Shield]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 5th-rank [[Spiritual Weapon]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Spiritual Guardian]].

**Source:** `= this.source` (`= this.source-type`)
