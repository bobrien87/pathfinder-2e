---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Healing]]", "[[Magical]]", "[[Spellheart]]", "[[Vitality]]"]
price: "{'gp': 4100}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A jyoti's feather is a shimmering red-and-gold feather that seems almost metallic, although it's delicate and flexible to the touch. Though most aren't made from true jyoti feathers, as the reclusive outsiders avoid visitors from the Universe, the creatures' connection to life energy lent these spellhearts their name.

- **Armor** You gain a +3 item bonus to saving throws against death effects and void energy.
- **Weapon** The weapon has the [[Vitalizing]] rune while the *feather* is affixed.

> [!danger] Effect: Jyoti's Feather   Armor

> [!danger] Effect: Jyoti's Feather   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Stabilize]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 5th-rank [[Vital Beacon]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Healing Well]]

**Source:** `= this.source` (`= this.source-type`)
