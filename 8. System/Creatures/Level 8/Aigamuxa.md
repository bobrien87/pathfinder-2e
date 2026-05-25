---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aigamuxa"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Scent]] (imprecise) 30 feet"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +16, Stealth +14"
abilityMods: ["+6", "+4", "+6", "-2", "+3", "+0"]
abilities_top:
  - name: "Limited Vision"
    desc: "An aigamuxa's eyes are located on the bottom of their feet, making it difficult for them to see. An aigamuxa is typically [[Blind]]. If they [[Seek]], they can see normally until the end of their turn."
  - name: "Weak Feet"
    desc: "If an aigamuxa takes damage from Striding or Stepping into hazardous terrain or a square with similar grounded hazards (such as caltrops), they can't Seek until the end of their next turn."
armorclass:
  - name: AC
    desc: "27; **Fort** +19, **Ref** +16, **Will** +13"
health:
  - name: HP
    desc: "140"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 2d8+9 slashing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (unarmed), **Damage** 2d12+9 piercing"
spellcasting: []
abilities_bot:
  - name: "Burrowed Ambush"
    desc: "`pf2:2` **Requirements** The aigamuxa is [[Hiding]] in dirt, sand, or another soft surface <br>  <br> **Effect** The aigamuxa makes a claw Strike against a creature within reach. On a hit, the aigamuxa automatically Grabs the creature. Whether or not they hit, the aigamuxa then Strides. If they have a creature grabbed, the creature moves with the aigamuxa."
  - name: "Burrowing Concealment"
    desc: "`pf2:2` **Requirements** The aigamuxa is standing on dirt, sand, or another soft surface <br>  <br> **Effect** The aigamuxa quickly digs into the surface and [[Hides]]. They leave their feet partially exposed, allowing them to see out from the surface. The aigamuxa can hold their breath for up to 10 minutes while hiding in this way."
  - name: "Swallow Whole"
    desc: "`pf2:1` Small, @Damage[(2d14+4)[bludgeoning]], Rupture 22 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Toss Up and Gulp Down"
    desc: "`pf2:1` **Requirements** A Small or smaller creature is [[Grabbed]] or [[Restrained]] in the aigamuxa's claw <br>  <br> **Effect** The aigamuxa tosses the creature into the air and distends their jaw to catch it in their mouth. The target is grabbed in the aigamuxa's jaws, and the aigamuxa attempts to [[Swallow it Whole]]. If the aigamuxa fails the Athletics check, the target misses the aigamuxa's mouth and falls 30 feet instead of being grabbed."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Aigamuxas are towering humanoids that stalk arid deserts in search of prey. Carnivorous and voracious, they hunt anything that moves but especially relish eating sentient creatures. Many Mwangi people incorrectly refer to aigamuxas as demons, while others more accurately describe them as having descended from giants. Aigamuxas resemble large humans with smooth hollows where their eyes should be, but their eyes are actually embedded in the soles of their feet. They sport long, sharp claws and teeth that they use to tear their prey apart once they catch them. A moving aigamuxa's odd gait resembles dancing more than a typical walk or run, but its speed is alarming, if difficult to correctly estimate at a distance.

An aigamuxa's unique physiology makes catching prey difficult, and most aigamuxas are constantly hungry. When pursuing prey, an aigamuxa must occasionally stop to lift its feet in order to regain their bearings. Most stand on their hands while looking around, which allows them to immediately backflip back into a run. An aigamuxa's eyes are generally resistant to the sands of their native desert habitats, but irritants such as chilies or caltrops can seriously impair their hunting ability, and desert travelers often carry a bag of these in case they need to deal with an aigamuxa.

Clever aigamuxas know that attacking wandering prey can be very dangerous, instead using their powerful hands to dig deep into sand dunes or dirt and wait to ambush passersby. Aigamuxas are particularly good at hiding in their home environments, and unfortunate travelers often don't notice the barely visible eyes of an aigamuxa until it's too late.

```statblock
creature: "Aigamuxa"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
