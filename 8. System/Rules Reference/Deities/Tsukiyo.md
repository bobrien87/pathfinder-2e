---
type: deity
source-type: "Remaster"
domains: "Moon, Repose, Soul, Delirium"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Soothe]], Rank 4: [[Peaceful Bubble]], Rank 5: [[Hallucination]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Tsukiyo has always been considered a complicated god in Tian Xia, constantly changing like the phases of the moon. Although closely associated with Shizuru, his worship is less evident across the land. Tsukiyo has little impact on state functions or annual events, but his influence runs deep in the daily lives and perspectives of Minkai. He is the Prince of the Moon, representing the night and the natural changes everyone experiences in life.

**Title** Prince of the Moon

**Areas of Concern** jade, the moon, spirits

**Edicts** provide aid and counsel without judgment to those who seek help, help the dead find their rest, amplify or help speak for the powerless and demonized

**Anathema** harm another out of envy, force aid on those who do not want it, inflict harmful mental effects on others as punishment, knowingly hurt the innocent, commit murder

**Religious Symbol** jade crescent with golden moon phases

**Sacred Animal** hare

**Sacred Colors** yellow and green

**Source:** `= this.source` (`= this.source-type`)
