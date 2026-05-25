---
type: deity
source-type: "Remaster"
domains: "Change, Glyph, Knowledge, Trickery"
favored-weapon: "Jaws, Greatclub"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Message Rune]], Rank 2: [[Blistering Invective]], Rank 4: [[Honeyed Words]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The protean lord of language evolution, lost words, and slang, Ydajisk manifests as a protean with six arms and a cobra's hood, surrounded by a cloud of drifting sounds, symbols, shapes, and myriad other sensory experiences that shift endlessly in and out of existence. Closer inspection reveals that their body is made from interlacing strands of poetic protean script. Ydajisk is also called the Mother of Tongues, though like all proteans, their gender changes as they will. Followers of Ydajisk are wanderers, reviving dead languages from ancient ruins, chronicling the dying tongues of cultures in decline, and discovering or inventing new words. All such knowledge acquired by agents of the Mother of Tongues passes into Ydajisk's realm, the Library of Stolen Words, where it is transcribed into books or stored in magical containers, alongside scrolls and tomes considered long lost by mortal scholars.

**Title** Mother of Tongues

**Areas of Concern** Language evolution, lost words, slang

**Edicts** Create using words, chronicle languages and prevent them from dying, help language evolve

**Anathema** Ban or discourage a language, explain a secret language or slang to outsiders, destroy literary works

**Religious Symbol** yawning maw drawn in lines of protean poetry

**Sacred Animal** myna

**Sacred Colors** azure, ivory

**Source:** `= this.source` (`= this.source-type`)
