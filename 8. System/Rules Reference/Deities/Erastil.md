---
type: deity
source-type: "Remaster"
domains: "Earth, Family, Nature, Wealth"
favored-weapon: "Longbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Wall Of Thorns]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Erastil is an old deity. Originally an elk-headed god of the hunt, he changed long ago to his current purview of family, farming, and trade, yet still holds to a few of the ancient ways. Currently, Erastil's concerns lie with community and the work that sustains those communities. Farming serves the basic needs of a people and requires them to maintain the crops. Families are the most basic unit of a community, with one generation caring for another. Trade requires enough to serve other communities, thus creating bonds of familiarity and interdependence. Yet behind this idyllic image lies the hard, oaken core of primal woods and steaming skin. This gives Erastil a multifaceted history, and while worshippers near cities and newer settlements worship the "softer" image of Erastil (an old man of the worshipper's ancestry), people in the wilderness or from very old civilizations still have the elk-headed depictions in their homes.

**Title** Old Deadeye

**Areas of Concern** family, farming, hunting, trade

**Edicts** care for your home and family, fulfill your duties, keep the peace, protect the community

**Anathema** abandon your home in its time of need, choose yourself over your community, tarnish your reputation, tell lies

**Religious Symbol** bow and arrow

**Sacred Animal** stag

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
