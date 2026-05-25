---
type: deity
source-type: "Remaster"
domains: "Darkness, Moon, Repose, Soul"
favored-weapon: "Bladed-scarf"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Vapor Form]], Rank 8: [[Uncontrollable Dance]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ashava, the True Spark, embodies moonlight, dancing, and lonely spirits. Dancing is Ashava's true love, and she encourages her followers to dance often. For some, she is little more than a patron of that art, but Ashava is also a guide, both in spirit and in the physical world. For the living, she leads the lonely out of their difficult times, her lights guiding lost wanderers back to safety. For the dead, her haunting moonlit dances lead lost and lonely spirits onward to their eternal judgment. She encourages her followers to steer those who are lost—whether in the wilderness or in their hearts—to where they need to go. Priests of Ashava are the dancing light that guides the way, but will-o'-wisps are anathema to Ashava, and her followers destroy these creatures wherever they are found.

**Title** The True Spark

**Areas of Concern** Dancers, lonely spirits, moonlight

**Edicts** Dance even when there is no music, cast light in places of darkness, lead the lost

**Anathema** Intentionally mislead someone, desecrate graves, abandon a creature in darkness

**Religious Symbol** dancing woman and moon

**Sacred Animal** wolf

**Sacred Colors** midnight blue, silver

**Source:** `= this.source` (`= this.source-type`)
