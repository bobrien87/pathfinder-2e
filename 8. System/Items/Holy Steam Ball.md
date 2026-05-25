---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Divine]]", "[[Holy]]", "[[Mental]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The *holy steam ball* is an odd-looking device that's nevertheless effective at reinforcing its user's mind against fiendish control. It's a hollow black-rubber ball with small, flexible twin tubes sticking out from its center. Sealed within the rubber ball is vapor made from a mixture of evaporated holy water and a special type of incense smoke. The tube's twin prongs are placed into the user's nostrils, after which the user squeezes the rubber ball to activate the device, forcing the vapor into the user's body through their nose. The holy power contained within the vapor strengthens the user's will against creatures that are weak to holy water, making it tougher for malevolent creatures to subvert the user's mind.

When the *holy steam ball* was first introduced in Mendev fifty years ago, few trusted it's efficacy. The nation had seen many charlatans peddle so-called "anti-demon" products, and most thought this was no different. Only when soldiers of the Mendevian Crusades used the ball and personally testified to its effectiveness did suspicion gave way to enthusiastic use. Nobody remembers who first invented the *holy steam ball*; they're likely lost to history because most initially thought it was a scam. After receiving endorsement from the Mendevian Crusade, a team of alchemists and inventors were able to determine the vapor's exact composition and mass produce them. The *holy steam ball*'s highly specialized purpose kept it from widespread use outside of the nations that once bordered the Worldwound. Yet with the return of the Whispering Tyrant in the past few years, the growing undead threat presents a new opportunity for more citizens to use *holy steam balls* for protection against the mind control powers of vampires and other undead.

After using a *holy steam ball*, you must refill it before the next use in a process that takes five minutes to complete.

**Activate** `pf2:1` (manipulate)

**Requirements** The *holy steam ball* is filled with evaporated [[Holy Water]] and incense smoke;

**Effect** You release the stored steam and smoke to grant yourself its protections. Each use of the *holy steam ball* lasts for 1 hour and gives you a +2 item bonus to Will saving throws against possession effects from fiends and undead and effects from fiends and undead that cause the [[Controlled]] condition.

> [!danger] Effect: Holy Steam Ball

**Source:** `= this.source` (`= this.source-type`)
