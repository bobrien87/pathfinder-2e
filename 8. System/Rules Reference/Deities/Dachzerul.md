---
type: deity
source-type: "Remaster"
domains: "Darkness, Luck, Secrecy, Trickery"
favored-weapon: "Rapier"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 3: [[Time Jump]], Rank 5: [[Hallucination]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Dachzerul believes in joy for everyone, especially himself. No pleasure should be denied, no joke interrupted, and no prank ruined by trivial matters such as safety or feelings. He is notable among the sahkil tormentors for his fickle moods, snapping from pleasant and exuberant to dark and obsessive within seconds, but can be instantly cheered by a deadly prank or a new object to obsess over. Towns unfortunate enough to draw his fleeting attention are hit by a deluge of wild phenomena such as raining frogs or water turning into vomit that stops just as suddenly as it started.

**Title** The Darkness Behind You

**Areas of Concern** Deadly pranks, stalkers, sudden death

**Edicts** Keep secrets from everyone, obtain what you desire, pursue your passions above all else

**Anathema** Choose safety over trickery, forewarn the target of a prank

**Religious Symbol** off-putting grin in a swath of darkness

**Sacred Animal** monkey

**Sacred Colors** orange, white

**Source:** `= this.source` (`= this.source-type`)
