---
type: deity
source-type: "Remaster"
domains: "Healing, Might, Repose, Water"
favored-weapon: "Meteor-hammer"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Haste]], Rank 5: [[Geyser]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Strength and Serenity teaches that the most important objective of all mortals is to grow strong, so that they will survive the rigors of existence and live well. To Izuyaku, wellness is a balance between the needs of the body and the needs of the mind; they encourage the devout to regularly exercise their body but also to rest and relax for equal periods. Appropriately, Izuyaku is often depicted as a gentle-faced human with both masculine and feminine features reclining in a hot spring bath, their stocky build having both muscle and fat in equal measure.

**Title** The Strength and Serenity

**Areas of Concern** balance, strength, health, and hot springs

**Edicts** keep communal bodies of water safe and clean, practice good hygiene, strengthen yourself and others physically or emotionally

**Anathema** intentionally spread a disease, neglect your personal wellness without good cause

**Religious Symbol** circle of stones surrounding a rippling pool of water

**Sacred Animal** snow monkey

**Sacred Colors** bright orange, vivid blue

**Source:** `= this.source` (`= this.source-type`)
