---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Perfection, Truth"
favored-weapon: "Shortbow"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Hypercognition]], Rank 4: [[Telepathy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Gruhastha the Keeper is a deity of understanding, peace, and the collective pursuit of enlightenment. The once-mortal nephew of [[Irori]] is believed to have ascended to godhood himself after creating the holy book *Azvadeva Pujila*, fully embodying all divine wisdom within the text. Originating in Vudra, the Keeper's faith has slowly gained popularity in the Inner Sea region, particularly in Jalmeray, where Irori already has a wide following. Gruhastha manifests as a human man with an idealized form, augmented with wings of red and green plumage and a golden mandala as a halo.

**Title** The Keeper

**Areas of Concern** enlightenment, the Vudrani holy book

**Edicts** work toward collective transcendence, expose and root out malicious lies, challenge oppression through education, protect knowledge, seek truth

**Anathema** deny a sincere student education, destroy knowledge, disrespect the traditions of those around you, willfully spread ignorance or wrong information

**Religious Symbol** mandala with books as compass points

**Sacred Animal** tortoise

**Sacred Color** teal, green

**Source:** `= this.source` (`= this.source-type`)
