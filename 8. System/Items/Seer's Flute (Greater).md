---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 460}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ivory flute is adorned with many carvings of eyes. Each has jade pupils and a semiprecious stone as its iris. The eyes flutter open and closed when the flute is played, as if it held the eyes of many independent beings. While playing the flute, you gain a +1 item bonus to Perception checks and Performance checks.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Guidance]], [[Read Aura]]
- **1st** [[Object Reading]]
- **2nd** [[Augury]], [[Object Reading]], [[See the Unseen]]
- **3rd** [[Clairaudience]], [[Hypercognition]], [[Wanderer's Guide]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
