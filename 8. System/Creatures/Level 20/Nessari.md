---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nessari"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+37; [[Greater Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Diabolic, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +34, Arcana +32, Athletics +33, Deception +39, Diplomacy +34, Intimidation +39, Religion +37, Society +36, Stealth +34"
abilityMods: ["+9", "+8", "+9", "+8", "+9", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Nessari Venom"
    desc: "**Saving Throw** DC 43 [[Fortitude]] save <br>  <br> **Maximum Duration** 10 rounds <br>  <br> **Stage 1** 6d6 poison damage and [[Drained]] 1 (1 round) <br>  <br> **Stage 2** 7d6 poison damage and [[Drained]] 2 (1 round) <br>  <br> **Stage 3** 8d6 poison damage and [[Drained]] 3 (1 round)"
  - name: "Shape Devils"
    desc: "The nessari reshapes a large number of orts within a 600-foot emanation into more powerful devils to swell Hell's legions. The nessari must have available the number of orts listed on the table below. <br>  <br> Devil LevelNumber of Orts4 or below45-687-8169-103211-126413-1412815-1625617-1851219-201.024The nessari can shape 100 orts per day, to a maximum of 1,100 orts in 11 days. Devils created in this way are in thrall to the nessari and follow its orders, with the exception of created nessaris or other devils of similar power, which are always independent. As a result, few nessaris choose to create peers. At the end of the Shape Devils activity, the nessari attempts an incredibly hard [[Religion]] check of the desired devil's level, with results as follows. <br> - **Critical Success** The nessari shapes two devils from the massed orts instead of one. <br> - **Success** The nessari shapes a devil of the desired type and level. <br> - **Failure** The devil shaped from the orts is 2 levels lower than the intended devil. <br> - **Critical Failure** The nessari fails to shape any devils and draws the ire of an archdevil for its waste of resources."
armorclass:
  - name: AC
    desc: "46; **Fort** +37, **Ref** +32, **Will** +35"
health:
  - name: HP
    desc: "335; regeneration 30 (deactivated by holy); **Immunities** fire; **Weaknesses** holy 15; **Resistances** physical 15 except silver, poison 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 30 (Deactivated by Holy)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Commander's Aura"
    desc: "100 feet. <br>  <br> Commanded or allied unholy creatures in the aura of lower level than the nessari gain a +1 circumstance bonus to attack rolls, damage rolls, AC, saves, and skill checks. <br>  <br> > [!danger] Effect: Commander's Aura"
  - name: "Frightful Presence"
    desc: "20 feet. DC 42 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike (Special)"
    desc: "`pf2:r` The nessari can make a Reactive Strike when a creature within reach uses a concentrate action, in addition to the usual trigger. The devil can disrupt triggering concentrate actions, and they disrupt actions on any hit, not only a critical hit. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +40 (`pf2:1`) (magical, poison, reach 10 ft., unarmed, unholy), **Damage** 4d10+17 piercing plus [[Pit Fiend Venom]]"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, magical, reach 10 ft., unarmed, unholy), **Damage** 4d6+17 slashing plus 2d6 spirit"
  - name: "Melee strike"
    desc: "Tail +36 (`pf2:1`) (magical, reach 10 ft., unholy), **Damage** 4d10+17 bludgeoning plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Wing +36 (`pf2:1`) (magical, reach 15 ft., unholy), **Damage** 4d6+17 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42, attack +34<br>**10th** [[Manifestation]]<br>**9th** [[Falling Stars]], [[Seize Soul]] (At Will)<br>**7th** [[Divine Decree]] (At Will)<br>**6th** [[Scrying]], [[Truesight]] (Constant)<br>**4th** [[Translocate]], [[Translocate]] (At Will), [[Wall of Fire]] (At Will)<br>**3rd** [[Fireball]] (At Will)<br>**2nd** [[Dispel Magic]] (At Will)"
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d10+17)[bludgeoning]], DC 43 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Fast Swoop"
    desc: "`pf2:1` The nessari Flies and makes a wing Strike at any point during its movement."
  - name: "Masterful Quickened Casting"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Effect** If the nessari's next action is to cast an 8th-rank or lower innate spell, reduce the number of actions to cast it by 1 (minimum 1 action)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When an army of devils invades to bathe a region in bloodshed and hellfire, it is likely that one of the nessaris masterminded the incursion. Cunning, powerful, and ruthless, nessaris often serve the archdevils directly. They rule infernal duchies, subjugate mortal worlds, and usurp infernal rivals using unparalleled despotism and calculated ferocity. To realize their tyrannical machinations, nessaris claim mortal souls that they corrupt into ort servants, which can then be shaped and transformed through infernal manipulation into the terrifying devils that form Hell's formidable legions. They often select the most wicked and vicious orts for their armies, drawing upon these lesser devils' depravity during powerful magical ceremonies to create hideous and terrifying abominations that can cow and eviscerate the nessari's enemies.

Each nessari is crafted deep within the nightmarish bowels of Nessus, the ninth layer of Hell, to serve the whims of archdevils and infernal dukes. Those nessaris that don't leave Nessus to command infernal legions in the upper layers of Hell often form the courts of Hell's elite, gathering cronies and sects that shape Hell's political landscape through subterfuge and manipulation. But many nessaris see themselves as living embodiments of hellfire, the all-encompassing wrath of Hell, and thus prefer to dwell in realms consumed by fire. In Avernus, Dis, Malebolge, Nessus, and Phlegethon, nessaris build vast citadels of brimstone wreathed in flame to lord over.

Rather than being above the constant power struggles of the diabolic ranks, nessaris are in the thick of it. Even apocalyptic schemes to conquer or despoil mortal worlds usually begin from a desire to claw a single rank up the immortal hierarchy of Hell. For this reason, the best, yet also most dangerous, ally against a nessari is the nessari next to them.

Nessaris tower over other devils, standing at least 16 feet tall, weighing over 1,000 pounds, and brandishing wingspans in excess of 20 feet.

Infernal Dukes
Elite members of Hell's political infrastructure and leadership hierarchy, the dukes of Hell are chosen from among the most tyrannical, oppressive, and conniving devils. While not all infernal dukes are nessaris, a nessari's natural disposition toward conquest and oppression often makes them an ideal candidate for this position. To create an infernal duke, adjust the nessari to be between 21st and 25th level. Because of their physical prowess, manipulative nature, and powerful spellcasting abilities, infernal dukes make excellent villains for long-running campaigns.

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Nessari"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
