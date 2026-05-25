---
type: deity
source-type: "Remaster"
domains: "Ambition, Freedom, Moon, Sun"
favored-weapon: "Greatpick"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 2: [[Penumbral Disguise]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Dajermube was once a mortal woman who led the rebellion against Mzali's Council of Mwanyisa when they tried to wipe out the worship of the Old Sun Gods. She was a descendant of the god Chohar, and divine power flowed through her veins. To help her people protect the knowledge of those deities, she attempted to ascend to godhood in the Temple of the Eclipse. Her ritual was interrupted as it reached its climax, and she was struck down by a crossbow bolt before the transformation was completed. As a result, she spent tormented centuries trapped between life and death until heroes freed the Temple of the Eclipse and enabled her apotheosis to resume.

**Title** Holder of Unquenchable Light

**Areas Of Concern** journeys, self-realization, shadows

**Edicts** push toward your own goals by striking your own path, try to help others achieve their goals when asked, draw upon all your resources

**Anathema** intentionally keep others from achieving honorable goals, support others to the exclusion of yourself or vice versa, use shadows to harm innocents

**Religious Symbol** moon partially eclipsing the sun

**Sacred Animal** lion

**Sacred Colors** gold, green, silver

**Source:** `= this.source` (`= this.source-type`)
