---
type: deity
source-type: "Remaster"
domains: "Family, Indulgence, Nature, Protection"
favored-weapon: "Katar, Fangs"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Animal Allies]], Rank 2: [[Slough Skin]], Rank 6: [[Cursed Metamorphosis]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Known to mortals as the Father of Serpents, Yig is an outlier among Great Old Ones in that he appears, at least on the surface, to pose little threat to mortals. The truth of the matter is somewhat more complicated, however, as the serpentine god enters intermittent feeding frenzies, during which even his most devout followers know to avoid attracting his attention, lest they become his next meal. When appearing before his congregation, Yig often takes on the form of a massive serpentine being with arms and legs, covered in green scales except for a distinctive silver crescent on his brow.

**Title** Cycles, procreation, serpents

**Areas of Concern** Cycles, procreation, serpents

**Edicts** Feast in the autumn, perform seasonal rituals, protect your home from trespassers

**Anathema** None

**Religious Symbol** coiled serpent with a crescent mark on its head

**Sacred Animal** snake

**Sacred Colors** green, silver

**Source:** `= this.source` (`= this.source-type`)
