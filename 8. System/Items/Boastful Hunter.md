---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Concussive]]", "[[Fatal aim d12]]", "[[Intelligent]]", "[[Primal]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +11; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (Common)

**Skills** Nature +9, Performance +10, Survival +11

**Int** +0, **Wis** +2, **Cha** +3

**Will** +11

Possessing a boisterous, proud demeanor, this *+1 jezail* is an aspiring big game hunter, always quick to share a tale of its bold adventures and predatory conquests—although the veracity of such tales is often questionable. A *boastful hunter* enjoys tracking and hunting animals of all kinds but takes particular pleasure in taking down large, dangerous, or rare animals. Against an animal, the boastful hunter deals 1d6 additional damage. On a critical hit against an animal, the boastful hunter also deals 1d6 persistent bleed damage.

A *boastful hunter* urges you to face off against tougher and tougher creatures—a challenge the ambitious rifle may not be adequate to deal with. If the *boastful hunter* goes one week without participating in a hunt against an animal of at least your level, it becomes bored. A bored *boastful hunter* complains incessantly and imposes a –1 item penalty to attack rolls against non-animal targets. A bored *boastful hunter* can be appeased by using it in combat against an animal of at least your level.

Unable to accept its own weaknesses, a *boastful hunter* blames any failed hunts on you, and considers remarks about its strength or quality a terrible insult. An insulted *boastful hunter* badmouths you to sentient creatures you interact with, imposing a –1 item penalty to Deception, Diplomacy, and Intimidation skill checks, and all attacks with it incur a misfire chance until the weapon is appeased. An insulted *boastful hunter* can be appeased by complimenting it and succeeding at a DC 21 [[Diplomacy]] check against its Will DC two days in a row. You can only attempt a Diplomacy check to appease the *boastful hunter* once each day.

**Source:** `= this.source` (`= this.source-type`)
