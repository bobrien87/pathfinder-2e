---
type: deity
source-type: "Remaster"
domains: "Creation, Magic, Moon, Nature"
favored-weapon: "Longbow, Shortbow"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Shape Wood]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Named after the ancient refuge of elven society on another planet, the Sovyrian Conclave includes all the traditional elven deities, as well as Alseta, a minor goddess of doors and transitions to be the patron of their aiudara (also known as elf gates). These six gods exemplify the positive traditions of elven society, including the study of magic, cohabitation with nature, the appreciation and creation of beautiful arts and crafts, and close friendships with other elves. Aiuvarins who wish a closer connection to their elven ancestry also worship the Sovyrian Conclave.

**Pantheon Members** Alseta, Calistria, Desna, Findeladlara, Ketephys, Yuelral

**Areas of Concern** elves, magic, nature, tradition

**Edicts** explore the worlds outside and within, learn and appreciate traditional elven arts, crafts, and magic

**Anathema** have an unhealthy obsession or attachment, irreparably damage the natural environment (such as by overhunting or strip mining)

**Religious Symbol** braided vine

**Source:** `= this.source` (`= this.source-type`)
