---
type: deity
source-type: "Remaster"
domains: "Creation, Pain, Repose, Sorrow"
favored-weapon: "Kukri"
divine-font: "Harm"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Earthbind]], Rank 5: [[Synaptic Pulse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Perhaps the cruelest of Hell's divinities, the Sadistic Angel shares certain characteristics with the velstracs who once resided in Hell—most notably, a drive to inflict physical pain upon living creatures. She does not inflict her torments out of anger or retribution; she practices her art with an unparalleled detachment and absence of emotion. Her followers are sadists, torturers who relish their grisly work, and those diabolists who summon velstracs rather than devils. While she bears the title of Queen of the Night and commands power commensurate with the others, Our Lady in Pain is content with her station and holds no ambitions beyond ensuring she can continue her tortures uninterrupted.

**Title** Our Lady of Pain

**Areas of Concern** Detachment, dispassion, pain

**Edicts** Push the boundaries of science and suffering, torture other creatures

**Anathema** Show or act on emotion, allow a plea for mercy to sway you

**Religious Symbol** halo of tears

**Sacred Animal** panther

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
