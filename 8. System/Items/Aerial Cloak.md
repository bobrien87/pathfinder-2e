---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This blue cloak is surprisingly light for its length and seems to catch wind bursts in its tail, flying out behind the wearer while cushioning falls and easing jumps. The sides of the cloak are slightly weighted, making it easy to grab ahold of when it fills with air. This cloak grants you a +1 item bonus to Athletics checks to [[Leap]] and a +1 item bonus to Acrobatics checks to [[Balance]] or [[Maneuver in Flight]].

**Activate—Fall Gently** R (concentrate, air)

**Frequency** once per day

**Trigger** You're falling

**Effect** The cloak catches the air and you grab onto its edges, utilizing the draft to guide you to safety. Treat your fall as 30 feet shorter and glide to a space of your choice at the bottom of your fall, which must be within 20 feet of where you would've landed

**Source:** `= this.source` (`= this.source-type`)
