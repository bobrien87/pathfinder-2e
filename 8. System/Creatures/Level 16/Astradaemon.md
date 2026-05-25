---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Astradaemon"
level: "16"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Darkvision]], [[Lifesense]] (precise) 30 feet, [[Truesight]] (precise) 60 feet"
languages: "Common, Daemonic (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +28, Athletics +32, Intimidation +33, Religion +26, Stealth +28, Survival +26"
abilityMods: ["+8", "+6", "+7", "+2", "+4", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Essence Drain"
    desc: "When an astradaemon hits with their claw, jaws, or tail, they drain the target's spiritual and vital essences. <br>  <br> The target takes 2d10 void damage and the astradaemon regains an equal number of Hit Points. The target must succeed at a DC 37 [[Fortitude]] save or become [[Doomed]] 1 and [[Drained]] 1. If the target was already drained or doomed, it instead increases both conditions' value by 1, to a maximum of 4."
armorclass:
  - name: AC
    desc: "39; **Fort** +27, **Ref** +30, **Will** +26"
health:
  - name: HP
    desc: "240; **Immunities** death effects, void; **Weaknesses** holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Bent Light"
    desc: "An astradaemon appears shifted from their true position, though still in the same space. Creatures targeting the astradaemon must succeed at a DC 11 flat check to do so, as if the astradaemon were [[Hidden]], even though the astradaemon remains observed. <br>  <br> Abilities that apply to the flat check against hidden creatures also apply against bent light."
  - name: "Soul Siphon"
    desc: "30 feet. <br>  <br> An astradaemon draws power from the souls of the recently slain. If a Small or larger living creature dies within their aura, the astradaemon gains 5 temporary Hit Points and a +1 status bonus to attack and damage rolls for 1 round, unless the creature was slain by an astradaemon's Devour Soul ability. <br>  <br> Incorporeal undead and living spirits that are traveling outside a body take 1d8 spirit damage each round within the daemon's aura as the astradaemon pulls in fragments of their soul. <br>  <br> > [!danger] Effect: Soul Siphon"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +32 (`pf2:1`) (magical, reach 10 ft., unarmed, unholy), **Damage** 3d6+8 piercing plus [[Essence Drain]] plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +32 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 2d6+8 slashing plus [[Essence Drain]]"
  - name: "Melee strike"
    desc: "Tail +32 (`pf2:1`) (magical, reach 15 ft., unholy), **Damage** 3d10+8 bludgeoning plus [[Essence Drain]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29<br>**8th** [[Pinpoint]]<br>**7th** [[Execute]], [[Interplanar Teleport]]<br>**6th** [[Truesight]] (Constant)<br>**4th** [[Translocate]], [[Translocate]] (At Will)"
abilities_bot:
  - name: "Devour Soul"
    desc: "`pf2:1` **Requirements** The astradaemon hasn't used an action with the attack trait yet this turn <br>  <br> **Effect** The astradaemon draws out and consumes the soul of a living creature they have [[Grabbed]]. <br>  <br> The creature must succeed at a DC 35 [[Fortitude]] save or instantly die. If it dies, the astradaemon gains 10 temporary Hit Points and a +2 status bonus to attack and damage rolls for 1 minute, or for 1 day if the victim was 15th level or higher. <br>  <br> A victim slain in this way can be returned to life normally. A creature that survives is temporarily immune for 1 minute. <br>  <br> > [!danger] Effect: Devour Soul <br>  <br> > [!danger] Effect: Devour Soul (Victim Level 15 or Higher)"
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These unnerving daemons represent death by direct assault against a soul or life-force. Rarely seen in the mortal Universe, astradaemons spend most of their time hunting the pathways between the living world and the afterlife. There, they capture migrating souls, snatching them from their rightful rewards or punishments and dragging them to Abaddon as tribute to their undying masters. These horrifying predators of the dead can also be found stalking the banks of the River of Souls in the Astral Plane, where they constantly hunt for new victims.

Denizens of the bleak and terrible plane of Abaddon, daemons are shaped by and devoted to the destruction of life in all its forms. They seek the death of every mortal being by the most painful and horrible means possible, in service to the Apocalypse Riders. Each kind of daemon represents a different way to die, and their powers are nearly always aimed at spreading that particular form of death. Through the use of these powers, they seek to drag all existence down into a pit of hopelessness and despair, and to commit all souls to oblivion.

While mortals who summon daemons usually seek to use the creatures' destructive and corrupting powers for their own ends, daemons always look for ways to spread fear, doubt, and despair wherever they go. Often, daemons disguise their plots as the workings of other fiends, knowing that such confusion compounds mortals' fear and keeps those mortals from bringing the most effective weapons. As a result, learned mortals sometimes refer to daemons as "riders" after their leaders or "soul mongers" after their largest industry.

While many fiends seek to tempt mortals into lives of nihilistic evil to increase their own numbers and power on their native planes, daemons are further driven by a supernatural hunger for mortal souls and use a variety of methods—not least of which is the cacodaemons' soul gems—to entrap them. On Abaddon and in other forbidding places across the multiverse, souls are simultaneously a delicacy, a trade good, and a source of magical power, and the daemons are among the greatest gluttons, merchants, and abusers of this spiritual "resource."

```statblock
creature: "Astradaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
