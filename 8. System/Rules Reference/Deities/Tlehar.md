---
type: deity
source-type: "Remaster"
domains: "Cities, Healing, Passion, Sun"
favored-weapon: "Morningstar"
divine-font: "Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Soothe]], Rank 3: [[Enthrall]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The old gods of the threefold sun were all but forgotten under the rule of Walkena, the child god. But Tlehar never despaired, for the dawn must forever represent hope to all good people who gaze upon it. She holds the Bright Lions of Mzali especially dear in her heart, since they were a ray of hope to her people even when she couldn't be. Thanks to them, citizens of Mzali and beyond have been reminded of her loving embrace, and once again awaken with resolve in their hearts.

**Title** The Rising Sun

**Areas of Concern** Iron, love, rebirth

**Edicts** Give yourself fully to everything you attempt, always maintain hope that tomorrow will be a better day, treasure every gift you are given by those who matter to you

**Anathema** Lose your motivation to your regrets, spread despair, treat a loved one poorly

**Religious Symbol** Semicircle of sunbeams

**Sacred Animal** lion

**Sacred Colors** gray, gold

**Source:** `= this.source` (`= this.source-type`)
