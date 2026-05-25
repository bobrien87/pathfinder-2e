---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gylou"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Greater Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Diabolic, Draconic, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +28, Arcana +25, Athletics +28, Deception +30, Diplomacy +28, Religion +26, Stealth +28"
abilityMods: ["+4", "+8", "+4", "+5", "+6", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "36; **Fort** +22, **Ref** +25, **Will** +28"
health:
  - name: HP
    desc: "240; **Immunities** fire; **Weaknesses** holy 10; **Resistances** physical 10 except silver, poison 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Reflexive Grab"
    desc: "`pf2:r` **Trigger** A creature leaves a square within the gylou's reach using a move action or attempts a melee Strike against the gylou <br>  <br> **Effect** The gylou lashes out with a tentacle, attempting to [[Grapple]] the triggering creature. If the triggering Strike was with a melee weapon, the attacking creature can Release the weapon to cause the gylou to automatically fail the Athletics check."
  - name: "Indispensable Savvy"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The gylou attempts a skill check but hasn't rolled yet <br>  <br> **Effect** The gylou demonstrates a preternatural ability for the task at hand. They use their Deception modifier for the triggering check and for all skill checks using the same skill thereafter until the next time the gylou uses this ability or until 24 hours have passed, whichever happens first."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +30 (`pf2:1`) (agile, finesse, magical, unarmed, unholy), **Damage** 3d8+12 slashing"
  - name: "Melee strike"
    desc: "Tentacle +30 (`pf2:1`) (finesse, magical, reach 10 ft., unarmed, unholy), **Damage** 3d12+12 bludgeoning plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28<br>**6th** [[Dominate]], [[Truesight]] (Constant)<br>**5th** [[Slither]]<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**3rd** [[Enthrall]] (At Will)<br>**2nd** [[Dispel Magic]]<br>**1st** [[Charm]], [[Illusory Object]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Encage in Tentacles"
    desc: "`pf2:1` **Requirements** The gylou has a Medium or smaller creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** The gylou transfers the grabbed creature into their lower body's net of encaging tentacles, freeing their limbs and tentacles to make Strikes. This has the same effects as [[Swallow Whole]] (Medium, @Damage[(2d12+12)[bludgeoning]], Rupture 30), except the encaged creature is not at risk of suffocation, and the gylou can bring the encaged creature with them when they cast [[Translocate]]. A gylou can have only one creature encaged at a time."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Though gylous are deeply entrenched in the expansive and complex machinations of Hell, they are highly skilled agents capable of nuanced diplomacy, masterful deception, physical finesse, and nearly any other tasks they set their minds to. This versatility has led to gylous becoming widespread throughout all layers of Hell, enabling them to filter key information to their masters regarding other devils' plots and schemes. Their allegiance is no secret, but their skills are so great that powerful devils employ one or more gylous regardless. While most gylous have a feminine form (combined with their role, this is the source of their common moniker of "handmaiden"), some have other gender presentations, and nearly all gylous take on carefully cultivated illusions to best suit the roles they fill. More often than not, gylous arise when lesser devils who have demonstrated exceptional utility and invaluable skills are uplifted into a new form, though on rare occasions they are shaped from the souls of evil mortals who showed unparalleled savvy within bureaucratic enterprises.

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Gylou"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
