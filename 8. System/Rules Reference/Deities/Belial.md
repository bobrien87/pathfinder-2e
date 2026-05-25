---
type: deity
source-type: "Remaster"
domains: "Change, Passion, Trickery, Zeal"
favored-weapon: "Ranseur"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[Humanoid Form]], Rank 3: [[Enthrall]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The lord of Hell's fourth layer, Phlegethon, is Belial. The Pale Kiss was created by Asmodeus as an object of adoration, with perfect form and beauty in the eyes of every creature. As a result, Belial has a virtually unlimited malleability of form, shifting between shapes almost constantly. His appearance is often as dualistic as his personality: half his body beautiful and half grotesque, much as he revels equally in pleasure and pain. As he is a creature of carnal desires, so are his followers: those who crave forbidden pleasures of the flesh but hide behind masks of respectability.

**Title** The Pale Kiss

**Areas of Concern** Adultery, deception, desire

**Edicts** Indulge your basest desires, create deadly weapons

**Anathema** Impede an act of high hedonism, become too attached to a lover or project

**Religious Symbol** two-toned devil mask

**Sacred Animal** goat

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
