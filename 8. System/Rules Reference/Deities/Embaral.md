---
type: deity
source-type: "Remaster"
domains: "Duty, Sorrow, Vigil, Water"
favored-weapon: "Wish-knife"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Slow]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Embaral and his fraternal twin brother Obari were once two of the many gods of Golarion's oceans, but both wanted to do more than simply oversee the waters under their command. Obari wished to explore and travel, while Embaral felt ill at ease with the changeability of water, drawn instead toward the stability of land. As Embaral sent gentle waves onto the shores adjoining his waters to better understand them, the goddess Vudravati was drawn to his persistence and patience, and the two fell in love.

But Vudravati also loved Embaral's twin, Obari. While the goddess was happy to take both as lovers, the jealous brothers soon went to war with each other for her affections. Obari sent typhoons to stir chaos in Embaral's waters, while Embaral stilled the winds raised by his brother and flooded the distant lands that Obari loved. The other ocean gods attempted to intervene to disastrous effect, with many losing their lives and immortality in the ensuing battles. As the war spilled across borders and waves, other gods of sea and storm abandoned their traditional demesnes to help shield mortals from the effects of the brothers' wrath. They created bays and seas, coordinating with gods of earth and stone to form peninsulas and islands, anything that the immortal powers could arrange to curtail the brother's influence and stay the fallout of their wrath. A few gods and immortal beings of the great waters fled Golarion altogether, seeking worlds and dominions that were not active battlegrounds for potent and violent immortal forces. But even when Embaral and Obari fought alone in isolated segments of Golarion's oceans, their war for dominance raged unabated, neither willing to be the first to retreat nor willing to sacrifice their emotional claims. Only Vudravati was able to stop the brothers' war, physically separating Embaral and Obari by lying between them in an endless sleep. Her decision instantly ended Embaral's anger, but the goddess as he knew her was lost to him, reborn as the land of Vudra.

**Title** The Flooded Heart

**Areas of Concern** heartache, passive resistance, and perseverance

**Edicts** oppose the unjust power of others through resistance, remain steadfast in the face of change, seek or give comfort to those suffering from heartache

**Anathema** act impulsively, change one's core principles without consideration, commit infidelity

**Religious Symbol** multicolored piece of sea glass

**Sacred Animal** dolphin

**Sacred Colors** light blue, seafoam green, white

**Source:** `= this.source` (`= this.source-type`)
