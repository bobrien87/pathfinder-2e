---
type: deity
source-type: "Remaster"
domains: "Earth, Introspection, Nature, Travel"
favored-weapon: "Halberd"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Mud Pit]], Rank 4: [[Elemental Gift]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Sunset Spires stands true, watching as the sun falls to greet the horizon each day. Just as they see the beauty in each sunset, they also see it in every creation that walks, swims, and flies upon Golarion. Keltheald spends most of their time traveling from one natural wonder to another, enjoying a different view every day. They most often take the form of a kestrel with vibrant wings the colors of a summer sunset, using this form to inconspicuously interact with the locations that they visit.

**Title** The Sunset Spires

**Areas of Concern** Natural formations, sunsets, vistas

**Edicts** Take the time to meditate at sunrise or sunset every day, seek out wondrous natural locations, travel to unfamiliar locales, create art reflective of natural beauty

**Anathema** Destroy natural locations and resources, willingly stay indoors for more than a day, never travel outside of your hometown

**Religious Symbol** coastal cliff at sunset

**Sacred Animal** kestrel

**Sacred Colors** orange, red

**Source:** `= this.source` (`= this.source-type`)
