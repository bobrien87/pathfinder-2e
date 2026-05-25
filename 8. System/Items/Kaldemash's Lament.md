---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Concealable]]", "[[Concussive]]", "[[Fatal d10]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Resembling little more than a simple iron pipe with a handle, *Kaldemash's Lament* is one of the most well-known star guns in all of Arcadia. Legends state the Crowned Regent Kaldemash helped forge one of the first star guns millennia ago. While the star gun served Kaldemash as a powerful weapon, its most notable achievement was the accidental killing of one of Kaldemash's greatest friends. This death is what caused the regent to recognize the true destructive power of the star guns and led to him developing the Star Code, a set of rules of engagement and proper use of firearms still in use in Arcadia today. Although Kaldemash never named the weapon himself, all legends that mention the weapon refer to it as *Kaldemash's Lament*.

The legendary weapon is a +3 major striking quickstrike advanced firearm with a range increment of 90 feet. It deals 4d6 force damage (with the major striking rune included) and has the concealable, concussive, and fatal d10 traits. You don't take a penalty when dealing nonlethal damage with the weapon. Like most star guns, *Kaldemash's Lament* uses magic to function and doesn't require ammunition or black powder.

If you use *Kaldemash's Lament* as part of a duel in which all parties are in agreement on the terms, the gun's supernatural instincts help you make the quickest draw. You roll twice and take the higher result on your initiative roll for the duel; this is a fortune effect. In addition, you can draw *Kaldemash's Lament* as a free action at the start of your turn during the duel. If you attempt to fire the star gun in bad faith at a dueling opponent once they have surrendered, been defeated, or the duel is over, *Kaldemash's Lament* flies out of your hand and you can't pick it up, hold it, or wield it for 10 minutes.

**Activate** `pf2:f` (concentrate)

**Trigger** You target a creature with an attack

**Effect** You adjust the damage that *Kaldemash's Lament* deals before firing. *Kaldemash's Lament*'s damage type changes to either electricity, fire, or force until you change the type again.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per minute

**Effect** You leave *Kaldemash's Lament* to fire on its own. You release the star gun and it begins to move independently, flying through the air and firing. You still gain the benefits of the gun's quickstrike rune while it's moving independently. It has a space of 5 feet but doesn't block or impede enemies attempting to move through that space. It always remains within 30 feet of you and intentionally resists being taken or otherwise moved; all attempts to Grab it fail. *Kaldemash's Lament* moves this way for 3 rounds, after which it returns to your hand. If you don't have a free hand to hold it, the gun instead holsters itself on your person.

While *Kaldemash's Lament* is moving independently, you can Sustain the activation to have it make a Strike against a creature. It makes a ranged Strike using your attack modifier while wielding it or a +31 bonus, whichever is higher. This attack increases your multiple attack penalty as normal, and the gun uses your multiple attack penalty when determining its attack bonus. Since the star gun is constantly moving and attempting to line up the appropriate shot, creatures it targets are [[Off Guard]] to the gun's attacks.

**Activate** `pf2:3` (concentrate, manipulate)

**Effect** You unleash a barrage of attacks in an instant. You deal Strike damage to all creatures in a @Template[type:cone|distance:30] (DC 45 [[Reflex]] save). This barrage counts as three attacks for your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
