---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Human|Human]]"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're ambitious, having accomplished more than your peers and always moving forward. You get two class abilities earlier than you normally could. Because you gain these abilities early, you can't select them again at a later level. One ability is the [[Fleet]] general feat. The second ability depends on your class.

- **Barbarian:** [[Raging Intimidation]]
- **Bard:** [[Well Versed]]
- **Monk:** [[Toughness]]
- **Sorcerer:** [[Cantrip Expansion]]

*Note: This heritage is from the Beginner Box and features non-standard heritage features*

**Source:** `= this.source` (`= this.source-type`)
