---
type: deity
source-type: "Remaster"
domains: "Change, Decay, Dreams, Nature"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 3: [[Wall Of Thorns]], Rank 7: [[Warp Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Xhamen-Dor, the living cancer, was born in the sewers beneath Carcosa, the alien city that is the home of Hastur. Somehow, this Great Old One was transported to Golarion within a comet, crashing into the bottom of a lake during the devastation of Earthfall. Physically, it manifests as a twisting and vaguely serpentine-shaped mass of bone, hair, and fungus.

The Inmost Blot, as Xhamen-Dor is also known, exists to conquer worlds by infecting the living with itself. Its victims, the seeded, enact its will and seek to spread its influence until the entire world is but an extension of Xhamen-Dor. Then, once only the seeded remain, Xhamen-Dor uses the last of the planet's energy to return to Carcosa, which in turn absorbs the world Xhamen-Dor has brought to it, allowing Carcosa to slowly grow.

**Title** The Inmost Blot

**Areas of Concern** Decay, parasites, transformation

**Edicts** Spread fungal growths, subtly infect others with knowledge of Xhamen-Dor

**Anathema** None

**Religious Symbol** sphere of tendrils

**Sacred Animal** none

**Sacred Colors** black, dark green

**Source:** `= this.source` (`= this.source-type`)
