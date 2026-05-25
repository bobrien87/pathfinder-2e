---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 645}"
usage: "wornarmbands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +17; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (Common and one other common or regional language)

**Skills** Intimidation +19, Sports Lore +17

**Int** +2, **Wis** +4, **Cha** +4

**Will** +17

Wrestler's armbands are a set of [[Armbands of Athleticism]] that have gained their own boisterous sapience. Often, such items aren't created intentionally but rather are the result of a truly charismatic champion whose heart and body are unusually strong wearing the armbands of athleticism on many adventures as their most important item. Eventually, the essence of their earnest and adventurous spirit has so thoroughly inundated the item it gains a matching spirit and will of its own. Such armbands view themselves as a tough, but fair, trainer for whomever inherits them next, inspiring you to new heights of athleticism. They also spoil for contests, telepathically calling out competitors on your behalf; typically the armbands won't challenge a foe you're unprepared to face, but particularly eager wrestler's armbands might have an unfortunate habit of overestimating your abilities and pushing you into a conflict that's beyond your proven capacity. These armbands have the following activation.

**Activate** R (concentrate)

**Frequency** once per minute

**Trigger** You succeed or critically succeed at an Athletics check

**Effect** The armbands taunt a creature you're competing with, boasting of your prowess and attempting an Intimidation check to [[Demoralize]] that creature.

**Source:** `= this.source` (`= this.source-type`)
