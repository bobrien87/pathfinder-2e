---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Divine]]", "[[Healing]]", "[[Intelligent]]", "[[Vitality]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +20; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (Common, Empyreal, and two other common languages)

**Skills** Diplomacy +21, Medicine +22, Religion +19, Sarenrae Lore +23

**Int** +2, **Wis** +5, **Cha** +4

**Will** +20

Prayer beads given prolonged exposure to spiritual energies at sacred Sarenite sites can attain sapience as *Dawnflower beads*. Other such objects hold the spirits of Sarenite priests who dedicated themselves to their work beyond death. *Dawnflower beads* function as a greater shining symbol. They don't re-attune to other deities but allow any divine spellcaster who isn't unholy to use them, though they attempt to talk their wielder out of morally questionable acts. Dawnflower beads have the following additional activations.

**Activate** Cast a Spell

**Effect** The beads cast 4th-rank [[Light]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** The beads cast 5th-rank [[Vital Luminance]].

**Source:** `= this.source` (`= this.source-type`)
