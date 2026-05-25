---
type: deity
source-type: "Remaster"
domains: "Knowledge, Repose, Sorrow, Vigil"
favored-weapon: "Staff"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Rewrite Memory]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Eldest of loneliness, sadness, and forgotten things, the Lost Prince spends most of his time brooding in the throne room of his crumbling tower. Although his precise origin is a hotly debated issue, the Lost Prince is known to hail from a place other than the First World. The melancholy lord doesn't speak of his home, and in fact he doesn't speak much at all, as he's prone to bouts of depression powerful enough to leach color from his surroundings and press his coterie of followers into respectful silence. Appearing as a gaunt, pale human man dressed in black finery, the Lost Prince bears vivid red runes on his brow and on the backs of his hands. He is studiously neutral in the schemes of the other Eldest, which makes his opinions and his favor particularly valuable.

**Title** The Melancholy Lord

**Areas of Concern** Forgotten things, sadness, solitude

**Edicts** Aid the depressed, wear somber clothing, maintain neutrality, ruminate on the past

**Anathema** Abandon someone who has no family, take public credit for your good deeds

**Religious Symbol** crumbling black tower

**Sacred Animal** raven

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
