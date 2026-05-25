---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]", "[[Sonic]]", "[[Spellheart]]"]
price: "{'gp': 340}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This two-pronged fork of metal emits a constant low hum, vibrating slightly when touched. The spell attack modifier of any spell cast by activating this item is +13, and the spell DC is 23.

- **Armor** You gain resistance 5 to sonic damage and a +2 item bonus to saving throws against effects with the auditory or sonic trait.
- **Weapon** After you cast a sonic spell by activating the fork, the weapon reverberates with trapped sound waves. Your next Strike causes the target to be [[Deafened]] for 3 rounds if it hits (or for 1 minute on a critical hit). If you don't make a Strike by the end of your next turn, the sound waves dissipate with no effect.

> [!danger] Effect: Resonating Fork   Armor

**Activate** Cast a Spell

**Effect** You cast [[Bullhorn]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 2nd-rank [[Biting Words]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Noise Blast]].

**Source:** `= this.source` (`= this.source-type`)
