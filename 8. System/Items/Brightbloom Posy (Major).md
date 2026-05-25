---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Magical]]", "[[Plant]]", "[[Spellheart]]"]
price: "{'gp': 36000}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Appearing as vibrant as the day they were picked, this cluster of flowers is arranged in a small spray, tied with a red satin ribbon. The spell DC of any spell cast by activating this item is 41.

- **Armor** You gain the ability to speak with flowers, as [[Speak with Plants]].
- **Weapon** (disease) After you cast a plant spell by activating the posy, pollen coats your weapon. Your next Strike causes the target to be [[Sickened]] 1 on a hit ([[Sickened]] 2 on a critical hit). If the creature attempts to recover, it sneezes rather than retching (rolling against the spellheart's spell DC). If you don't make a Strike by the end of your next turn, the pollen becomes inert. Plant creatures are immune.

**Activate** Cast a Spell

**Effect** You cast [[Tangle Vine]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 6th-rank [[Petal Storm]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Burning Blossoms]].

**Source:** `= this.source` (`= this.source-type`)
