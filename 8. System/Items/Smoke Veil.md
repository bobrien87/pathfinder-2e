---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Fire]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Smoke veils* are wigs or headdresses made of flame and ash, giving the wearer a burning coil of fiery hair and concealing their face behind a smoldering, omnipresent haze of smoke and sparking embers. You can use the veil to go unrecognized by hiding your face so that you can attempt Deception checks to [[Impersonate]] without needing a disguise kit. When you do so, it takes you only 1 minute to create the disguise, and you gain a +1 item bonus to the check. You still need a disguise kit and the full time if you're using cosmetics and other props to change other aspects of your disguise, or if Impersonating a specific person.

**Activate—Blazing Stare** `pf2:1` (concentrate)

**Requirements** You dealt fire damage to a target you can see within 30 feet with your most recent action this turn

**Effect** You set your fiery gaze on your target, eyes burning within a cloud of ash and cinder. Roll an Intimidation check to [[Demoralize]] the target. Demoralize loses the auditory trait and gains the visual trait, and you don't take a penalty when you attempt to Demoralize a creature that doesn't understand your language.

**Source:** `= this.source` (`= this.source-type`)
