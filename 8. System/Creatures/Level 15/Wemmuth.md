---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wemmuth"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet"
languages: "Aklo, Fey (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +29, Deception +28, Stealth +30, Survival +27"
abilityMods: ["+8", "+6", "+6", "-2", "+4", "+2"]
abilities_top:
  - name: "Thorny Mass"
    desc: "Whenever a creature within 10 feet attempts a melee attack against a wemmuth or uses Acrobatics to [[Tumble Through]] its space, that creature takes @Damage[(1d12+10)[piercing]] damage (DC 36 [[Reflex]] save)."
armorclass:
  - name: AC
    desc: "37; **Fort** +27, **Ref** +27, **Will** +24"
health:
  - name: HP
    desc: "335; **Weaknesses** cold 20, slashing 15"
abilities_mid:
  - name: "Blood Leech"
    desc: "`pf2:r` **Trigger** The wemmuth deals damage to a creature with Constrict <br>  <br> **Effect** The wemmuth heals a number of Hit Points equal to half the total damage dealt by Constrict."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Vine +29 (`pf2:1`) (fatal d12, reach 15 ft., sweep), **Damage** 4d12+10 bludgeoning plus [[Improved Grab]]"
  - name: "Ranged strike"
    desc: "Boulder +27 (`pf2:1`) (fatal d12, range 60 ft.), **Damage** 4d10+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(2d12+10)[bludgeoning]] damage, DC 36 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Engulf"
    desc: "`pf2:2` DC 36 [[Reflex]] save, 4d8 bludgeoning damage, `act escape dc=33`, Rupture 36 <br>  <br> The monster Strides up to double its Speed and can move through the spaces of any creatures in its path. Any creature of the monster's size or smaller whose space the monster moves through can attempt a Reflex save with the listed DC to avoid being engulfed. A creature unable to act automatically critically fails this save. If a creature succeeds at its save, it can choose to be either pushed aside (out of the monster's path) or pushed in front of the monster to the end of the monster's movement. The monster can attempt to Engulf the same creature only once in a single use of Engulf. The monster can contain as many creatures as can fit in its space. <br>  <br> A creature that fails its save is pulled into the monster's body. It is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The creature takes the listed amount of damage when first engulfed and at the end of each of its turns while it's engulfed. An engulfed creature can get free by [[Escaping]] against the listed escape DC. An engulfed creature can attack the monster engulfing it, but only with unarmed attacks or with weapons of light Bulk or less. The engulfing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the engulfed creature cuts itself free. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> A creature that gets free by either method can immediately breathe and exits the swallowing monster's space. <br>  <br> If the monster dies, all creatures it has engulfed are automatically released as the monster's form loses cohesion."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Fertilized by large quantities of spilled blood, such as that found on bloodstained battlefields or in the war-torn regions surrounding besieged cities, wemmuths are vile swaths of vines that draw sustenance from mortal suffering, lapping up blood like water. They possess a rudimentary intelligence and an unquenchable thirst for blood, lying in wait for most of their lives and growing to incredible size in the bloody soil of their grisly homes. A wemmuth's body comprises vines that are scarcely thicker than rope, and a single adult wemmuth system consists of six tons of vines, enough to stretch for 6,000 feet if laid out from end to end in a single straight line. Wemmuths never orient themselves this way, however, instead preferring to wrap themselves into massive mounds approximately 15 feet across and equally thick. The creature condenses its entire mass into a sphere of sharp thorns and lashing vines, resembling a hateful tumbleweed the size of an elephant. Wemmuths commonly dig up massive boulders or entire trees from the ground and incorporate them into their rolling mass, using these objects to bolster their defense against many forms of attack or to hurl at faraway foes with terrifying precision.

Some speculate that wemmuths are a form of diabolical corruption let loose upon Golarion by House Thrune of Cheliax, perhaps as a scorched earth tactic against their rivals. Influential nobles from Nirmathas and Molthune both point fingers at one another for the wemmuth's creation, Nirmathas citing Molthune's close ties to infernal Cheliax and Molthune blaming the primal magic commonly employed by Nirmathas's many druids and rangers. Several Varisian tales describe creatures closely matching the wemmuth's description attempting to apprehend a famous folk trickster, while crusaders from Mendev adhere to the belief that the wemmuths were a blight unleashed upon Golarion by Deskari, former demon lord of locusts, before his defeat at the hands of mortal heroes.

```statblock
creature: "Wemmuth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
