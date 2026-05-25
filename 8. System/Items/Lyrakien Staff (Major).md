---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 8600}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A crystalline sphere, swirling with constantly shifting constellations, sits atop a *lyrakien staff*, a silver shaft that sparkles with the gentle glow of starlight. Desnans first created the staves, inspired by the music- and freedom-loving lyrakien azatas, but these staves are popular with spellcasters of all faiths who like travel, art, or the stars. While wielding a lyrakien staff, you gain a +2 circumstance bonus on saving throws against incapacitation effects.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Guidance]], [[Summon Instrument]]
- **1st** [[Concordant Choir]]
- **2nd** [[Guiding Star]], [[Sure Footing]]
- **3rd** [[Dream Message]], [[Safe Passage]], [[Wanderer's Guide]]
- **4th** [[Concordant Choir]], [[Dream Message]], [[Unfettered Movement]], [[Sure Footing]]
- **5th** [[Safe Passage]], [[Summon Celestial]] (azatas only)
- **6th** [[Concordant Choir]], [[Zealous Conviction]]
- **7th** [[Cosmic Form]], [[Sure Footing]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
