---
type: deity
source-type: "Remaster"
domains: "Fire, Healing, Sun, Truth"
favored-weapon: "Scimitar"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 3: [[Fireball]], Rank 4: [[Wall Of Fire]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Like the light of dawn, Sarenrae spreads warmth across the world and into the hearts of its inhabitants. Burning passion, exuberant joviality, and fierce determination all rise at the goddess's influence. Sarenrae is one of the most popular deities on Golarion, with vast amounts of worshippers found from Tian Xia to Taldor. Beyond her warmth, her focus on redemption draws many to her faith. There is always room under her roof for those who have seen the error of their ways and wish to make amends, especially if they'll also pass their story onto others to prevent them from making the same mistakes.

**Title** The Dawnflower

**Areas of Concern** healing, honest redemption, the sun

**Edicts** destroy the Spawn of Rovagug, protect allies, provide aid to the sick and wounded, seek and allow redemption

**Anathema** create undead, lie, deny a repentant creature an opportunity for redemption, fail to strike down evil

**Religious Symbol** angelic ankh

**Sacred Animal** dove

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
